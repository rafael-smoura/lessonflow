/* ==========================================================================
   ENVIRONMENT CONFIGURATION AND ENDPOINTS DETECTION ENGINE
   ========================================================================== */
const API_BASE_URL = window.location.origin.includes("127.0.0.1") || window.location.origin.includes("localhost")
    ? "http://127.0.0.1:17001"
    : "https://lessonflow-backend.onrender.com"; // <-- Production Render base server target URL

// Global architecture states for orchestration
let currentPage = 1;
const limitPerPage = 10;
let searchTimeout;

/* ==========================================================================
   TAB ROUTER ENGINE CONTROLLER
   ========================================================================== */
function switchTab(tabName) {
    document.querySelectorAll(".tab-content").forEach(el => el.classList.add("d-none"));
    
    if (tabName === "list") {
        document.getElementById("tab-list").classList.remove("d-none");
        fetchLessonPlans();
    } else if (tabName === "form") {
        document.getElementById("tab-form").classList.remove("d-none");
    }
}

/* ==========================================================================
   SEARCH FILTERS QUERY HANDLERS
   ========================================================================== */
function resetPageAndFetch() {
    currentPage = 1;
    fetchLessonPlans();
}

function changePage(direction) {
    currentPage += direction;
    fetchLessonPlans();
}

function clearFilters() {
    document.getElementById("filter-value").value = "";
    document.getElementById("filter-type").value = "title";
    document.getElementById("sort-order").value = "created_at|desc";
    resetPageAndFetch();
}

/* ==========================================================================
   REST PARAMS CONSUMER PIPELINE (FLASK DISPATCHER)
   ========================================================================== */
async function fetchLessonPlans() {
    const filterType = document.getElementById("filter-type").value;
    const filterValue = document.getElementById("filter-value").value.trim();
    const sortValue = document.getElementById("sort-order").value;
    
    const [sortBy, order] = sortValue.split("|");

    // Dynamic processing matching contract specifications for Flask criteria routing
    let url = `${API_BASE_URL}/lesson-plans?page=${currentPage}&per_page=${limitPerPage}&sort_by=${sortBy}&order=${order}`;
    
    if (filterValue !== "") {
        if (filterType === "title") {
            url += `&search=${encodeURIComponent(filterValue)}`;
        } else {
            url += `&${filterType}=${encodeURIComponent(filterValue)}`;
        }
    }

    try {
        const response = await fetch(url);
        const result = await response.json();
        
        renderTable(result.data || []);
        updatePaginationControls(result.total || 0, result.page || currentPage);
    } catch (error) {
        console.error("Critical communications malfunction with Flask API:", error);
    }
}

/* ==========================================================================
   TABLE & VIEW SYNCHRONIZATION ENGINES
   ========================================================================== */
function renderTable(plans) {
    const container = document.getElementById("lesson-plans-container");
    container.innerHTML = "";

    if (plans.length === 0) {
        container.innerHTML = `<tr><td colspan="5" class="text-center text-muted py-4">No lesson plans found corresponding to the active parameters.</td></tr>`;
        return;
    }

    plans.forEach(plan => {
        const tagsHtml = plan.tags 
            ? plan.tags.split(",").map(t => `<span class="tag-pill">${t.trim()}</span>`).join("")
            : "<span class='text-muted small'>None</span>";

        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td class="px-4 fw-semibold text-white">${plan.title}</td>
            <td><span class="badge bg-secondary">${plan.discipline}</span></td>
            <td class="text-light">${plan.planned_date || "Not specified"}</td>
            <td>${tagsHtml}</td>
            <td class="px-4 text-end">
                <button class="action-icon-btn" onclick="editPlan(${plan.id})" title="Edit plan">✏️</button>
                <button class="action-icon-btn" onclick="deletePlan(${plan.id})" title="Delete plan">🗑️</button>
            </td>
        `;
        container.appendChild(tr);
    });
}

function updatePaginationControls(totalItems, serverPage) {
    const totalPages = Math.ceil(totalItems / limitPerPage) || 1;
    currentPage = serverPage;

    const startItem = totalItems === 0 ? 0 : (currentPage - 1) * limitPerPage + 1;
    const endItem = Math.min(currentPage * limitPerPage, totalItems);

    document.getElementById("pagination-text").innerText = `Showing ${startItem}-${endItem} of ${totalItems} operational records`;
    
    document.getElementById("btn-prev").disabled = currentPage <= 1;
    document.getElementById("btn-next").disabled = currentPage >= totalPages;
}

/* ==========================================================================
   CRUD ACTION HANDLERS Lifecycle
   ========================================================================== */
async function handleFormSubmit(event) {
    event.preventDefault();
    const id = document.getElementById("lesson-plan-id").value;

    const payload = {
        title: document.getElementById("title").value,
        discipline: document.getElementById("discipline").value,
        planned_date: document.getElementById("planned_date").value,
        objective: document.getElementById("objective").value,
        summary: document.getElementById("summary").value,
        contents: document.getElementById("contents").value,
        support_resources: document.getElementById("support_resources").value,
        tags: document.getElementById("tags").value
    };

    const url = id ? `${API_BASE_URL}/lesson-plans/${id}` : `${API_BASE_URL}/lesson-plans`;
    const method = id ? "PUT" : "POST";

    try {
        const response = await fetch(url, {
            method: method,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        if (response.ok) {
            alert("Payload transaction complete: Record saved successfully!");
            document.getElementById("lesson-plan-form").reset();
            document.getElementById("lesson-plan-id").value = "";
            switchTab("list");
        } else {
            const err = await response.json();
            alert("Transaction error: " + JSON.stringify(err.errors || err.message));
        }
    } catch (error) {
        console.error("Form transmission fault occurred:", error);
    }
}

/* ==========================================================================
   LLM AI COGNITIVE SUBSYSTEM INTEGRATION (SMART ASSIST)
   ========================================================================== */
async function generateAIRecommendations() {
    const title = document.getElementById("title").value;
    const discipline = document.getElementById("discipline").value;
    const summary = document.getElementById("summary").value;

    if (!title || !discipline || !summary) {
        alert("Preconditional failure: Title, Discipline, and Summary data must be populated before invoking AI analysis!");
        return;
    }

    const aiButton = document.getElementById("btn-smart-assist");
    const aiFields = document.querySelectorAll(".ai-field");

    aiButton.disabled = true;
    aiButton.innerText = "⏳ Querying Pedagogical LLM Core...";
    aiFields.forEach(field => field.classList.add("loading-skeleton"));

    try {
        const response = await fetch(`${API_BASE_URL}/lesson-plans/ai-recommendations`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ title, discipline, summary })
        });
        const result = await response.json();

        if (response.ok && result.data) {
            document.getElementById("contents").value = result.data.contents || "";
            document.getElementById("support_resources").value = result.data.support_resources || "";
            document.getElementById("tags").value = result.data.tags || "";
        }
    } catch (error) {
        console.error("Inference sequence failure on AI context generation:", error);
        alert("Cognitive system timeout or parsing error. Please verify terminal server status logs.");
    } finally {
        aiButton.disabled = false;
        aiButton.innerText = "Generate Recommendations";
        aiFields.forEach(field => field.classList.remove("loading-skeleton"));
    }
}

/* ==========================================================================
   RECORD MODIFICATION & DELETION DISPATCHERS
   ========================================================================== */
async function editPlan(id) {
    try {
        const response = await fetch(`${API_BASE_URL}/lesson-plans/${id}`);
        if (!response.ok) return;
        const plan = await response.json();

        document.getElementById("lesson-plan-id").value = plan.id;
        document.getElementById("title").value = plan.title || "";
        document.getElementById("discipline").value = plan.discipline || "";
        document.getElementById("planned_date").value = plan.planned_date || "";
        document.getElementById("objective").value = plan.objective || "";
        document.getElementById("summary").value = plan.summary || "";
        document.getElementById("contents").value = plan.contents || "";
        document.getElementById("support_resources").value = plan.support_resources || "";
        document.getElementById("tags").value = plan.tags || "";

        document.getElementById("form-title").innerText = "Edit Lesson Plan Target";
        switchTab("form");
    } catch (error) {
        console.error("Extraction fault during record local caching stage:", error);
    }
}

async function deletePlan(id) {
    if (!confirm("Destructive action warning: Are you completely certain you want to purge this record from memory?")) return;
    try {
        const response = await fetch(`${API_BASE_URL}/lesson-plans/${id}`, { method: "DELETE" });
        if (response.ok) { 
            fetchLessonPlans(); 
        }
    } catch (error) {
        console.error("Purging lifecycle execution error:", error);
    }
}

/* ==========================================================================
   INITIALIZATION RUNTIME ATTACHMENT
   ========================================================================== */
document.addEventListener("DOMContentLoaded", () => {
    fetchLessonPlans();

    // Debounce processing logic to protect thread pools from input spamming events
    document.getElementById("filter-value").addEventListener("input", () => {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(resetPageAndFetch, 300);
    });
});