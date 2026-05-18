const API_BASE_URL = "http://127.0.0.1:17001";

let currentLang = localStorage.getItem("lang") || "en";

/* =========================================
   TRANSLATIONS
========================================= */

const translations = {
    en: {
        nav_plans: "My Plans",
        nav_new: "New Plan",
        list_title: "Registered Lesson Plans",
        btn_create: "+ Create New Plan",
        opt_title: "🔍 By Title",
        opt_discipline: "📚 By Discipline",
        opt_tag: "🏷️ By Tag",
        search_placeholder: "Type to search and see suggestions...",
        btn_clear: "Clear",
        th_title: "Title",
        th_discipline: "Discipline",
        th_date: "Planned Date",
        th_tags: "Tags",
        th_actions: "Actions",
        form_title_new: "Create New Lesson Plan",
        form_title_edit: "Edit Lesson Plan",
        lbl_title: "Class Title *",
        lbl_discipline: "Discipline *",
        lbl_objective: "Objective *",
        lbl_summary: "Syllabus / Summary *",
        lbl_date: "Planned Date *",
        ai_title: "✨ Smart Assist (AI)",
        ai_subtitle: "Generate suggestions for contents, resources, and tags based on the summary.",
        btn_ai: "Generate Recommendations",
        lbl_contents: "Suggested Contents",
        lbl_resources: "Support Resources",
        lbl_tags: "Tags (Comma separated)",
        tags_placeholder: "ex: algebra, equations, math",
        btn_cancel: "Cancel",
        btn_save: "Save Plan",
        btn_lang_toggle: "🇧🇷 PT-BR",
        alert_ai_fields: "Please fill in Title, Discipline, and Summary before using the AI.",
        alert_ai_error: "AI Service Error: ",
        alert_api_fail: "Could not connect to AI service.",
        alert_save_success: "Lesson plan saved successfully!",
        alert_delete_confirm: "Are you sure you want to permanently delete this lesson plan?",
        alert_delete_success: "Lesson plan removed successfully!",
        no_plans: "No lesson plans found.",
        btn_edit: "Edit",
        btn_delete: "Delete"
    },

    pt: {
        nav_plans: "Meus Planos",
        nav_new: "Novo Plano",
        list_title: "Planos de Aula Cadastrados",
        btn_create: "+ Criar Novo Plano",
        opt_title: "🔍 Por Título",
        opt_discipline: "📚 Por Disciplina",
        opt_tag: "🏷️ Por Tag",
        search_placeholder: "Digite para buscar e ver sugestões...",
        btn_clear: "Limpar",
        th_title: "Título",
        th_discipline: "Disciplina",
        th_date: "Data Prevista",
        th_tags: "Tags",
        th_actions: "Ações",
        form_title_new: "Cadastrar Novo Plano de Aula",
        form_title_edit: "Editar Plano de Aula",
        lbl_title: "Título da Aula *",
        lbl_discipline: "Disciplina *",
        lbl_objective: "Objetivo *",
        lbl_summary: "Ementa / Resumo *",
        lbl_date: "Data Prevista *",
        ai_title: "✨ Smart Assist (IA)",
        ai_subtitle: "Gere sugestões de conteúdos, recursos e tags baseados na ementa.",
        btn_ai: "Gerar Recomendações",
        lbl_contents: "Conteúdos Sugeridos",
        lbl_resources: "Recursos de Apoio",
        lbl_tags: "Tags (Separadas por vírgula)",
        tags_placeholder: "ex: algebra, equacoes, matematica",
        btn_cancel: "Cancelar",
        btn_save: "Salvar Plano",
        btn_lang_toggle: "🇺🇸 EN-US",
        alert_ai_fields: "Preencha Título, Disciplina e Resumo antes de usar a IA.",
        alert_ai_error: "Erro da IA: ",
        alert_api_fail: "Não foi possível conectar com a IA.",
        alert_save_success: "Plano salvo com sucesso!",
        alert_delete_confirm: "Deseja realmente excluir este plano?",
        alert_delete_success: "Plano removido com sucesso!",
        no_plans: "Nenhum plano encontrado.",
        btn_edit: "Editar",
        btn_delete: "Excluir"
    }
};

/* =========================================
   THEME
========================================= */

function loadTheme() {
    const savedTheme = localStorage.getItem("theme") || "dark";

    document.documentElement.setAttribute("data-bs-theme", savedTheme);

    const themeBtn = document.getElementById("btn-theme");

    themeBtn.innerText = savedTheme === "dark"
        ? "☀️"
        : "🌙";
}

function toggleTheme() {
    const htmlTag = document.documentElement;
    const currentTheme = htmlTag.getAttribute("data-bs-theme");

    const newTheme = currentTheme === "dark"
        ? "light"
        : "dark";

    htmlTag.setAttribute("data-bs-theme", newTheme);

    localStorage.setItem("theme", newTheme);

    document.getElementById("btn-theme").innerText =
        newTheme === "dark"
            ? "☀️"
            : "🌙";
}

/* =========================================
   LANGUAGE
========================================= */

function toggleLanguage() {
    currentLang = currentLang === "en"
        ? "pt"
        : "en";

    localStorage.setItem("lang", currentLang);

    applyTranslations();

    fetchLessonPlans();
}

function applyTranslations() {
    const langData = translations[currentLang];

    document.querySelectorAll("[data-i18n]").forEach(element => {
        const key = element.getAttribute("data-i18n");

        if (langData[key]) {
            element.innerText = langData[key];
        }
    });

    document.querySelectorAll("[data-i18n-placeholder]").forEach(element => {
        const key = element.getAttribute("data-i18n-placeholder");

        if (langData[key]) {
            element.setAttribute("placeholder", langData[key]);
        }
    });

    document.getElementById("btn-language").innerText =
        langData.btn_lang_toggle;

    const planId = document.getElementById("plan-id").value;

    document.getElementById("form-title").innerText =
        planId
            ? langData.form_title_edit
            : langData.form_title_new;
}

/* =========================================
   TABS
========================================= */

function switchTab(tab) {

    const sectionList = document.getElementById("section-list");
    const sectionForm = document.getElementById("section-form");

    const navList = document.getElementById("nav-list-tab");
    const navForm = document.getElementById("nav-form-tab");

    if (tab === "list") {

        sectionList.style.display = "block";
        sectionForm.style.display = "none";

        navList.classList.add("active");
        navForm.classList.remove("active");

        fetchLessonPlans();

    } else {

        sectionList.style.display = "none";
        sectionForm.style.display = "block";

        navList.classList.remove("active");
        navForm.classList.add("active");

        if (!document.getElementById("plan-id").value) {

            document.getElementById("lesson-plan-form").reset();

            document.getElementById("form-title").innerText =
                translations[currentLang].form_title_new;
        }
    }
}

/* =========================================
   FETCH LESSON PLANS
========================================= */

async function fetchLessonPlans() {

    const filterType = document.getElementById("filter-type").value;
    const filterValue = document.getElementById("filter-value").value;

    let url = `${API_BASE_URL}/lesson-plans?page=1&per_page=50`;

    if (filterValue) {
        url += `&${filterType}=${encodeURIComponent(filterValue)}`;
    }

    try {

        const response = await fetch(url);
        const result = await response.json();

        const tbody = document.getElementById("lesson-plans-table-body");

        tbody.innerHTML = "";

        if (result.data && result.data.length > 0) {

            result.data.forEach(plan => {

                tbody.insertAdjacentHTML(
                    "beforeend",
                    `
                    <tr>
                        <td>
                            <strong>${plan.title}</strong>
                        </td>

                        <td>
                            <span class="badge bg-secondary">
                                ${plan.discipline}
                            </span>
                        </td>

                        <td>
                            ${plan.planned_date}
                        </td>

                        <td>
                            <small class="text-muted">
                                ${plan.tags || "-"}
                            </small>
                        </td>

                        <td class="text-center">
                            <div class="btn-group btn-group-sm">

                                <button
                                    class="btn btn-outline-primary"
                                    onclick="editPlan(${plan.id})"
                                >
                                    ${translations[currentLang].btn_edit}
                                </button>

                                <button
                                    class="btn btn-outline-danger"
                                    onclick="deletePlan(${plan.id})"
                                >
                                    ${translations[currentLang].btn_delete}
                                </button>

                            </div>
                        </td>
                    </tr>
                    `
                );
            });

            updateSuggestions(result.data, filterType);

        } else {

            tbody.innerHTML = `
                <tr>
                    <td colspan="5" class="text-center text-muted p-4">
                        ${translations[currentLang].no_plans}
                    </td>
                </tr>
            `;
        }

    } catch (error) {

        console.error("Error fetching lesson plans:", error);
    }
}

/* =========================================
   SUGGESTIONS
========================================= */

function updateSuggestions(plans, type) {

    const datalist = document.getElementById("search-suggestions");

    datalist.innerHTML = "";

    let suggestions = [];

    plans.forEach(plan => {

        if (type === "search" && plan.title) {
            suggestions.push(plan.title);
        }

        if (type === "discipline" && plan.discipline) {
            suggestions.push(plan.discipline);
        }

        if (type === "tag" && plan.tags) {

            plan.tags
                .split(",")
                .forEach(tag => suggestions.push(tag.trim()));
        }
    });

    const uniqueSuggestions = [...new Set(suggestions)];

    uniqueSuggestions
        .slice(0, 6)
        .forEach(term => {

            datalist.insertAdjacentHTML(
                "beforeend",
                `<option value="${term}"></option>`
            );
        });
}

/* =========================================
   FILTERS
========================================= */

function handleFilterTypeChange() {

    document.getElementById("filter-value").value = "";

    fetchLessonPlans();
}

function clearFilter() {

    document.getElementById("filter-value").value = "";

    fetchLessonPlans();
}

/* =========================================
   AI ASSIST
========================================= */

async function generateAIRecommendations() {

    const title = document.getElementById("title").value;
    const discipline = document.getElementById("discipline").value;
    const summary = document.getElementById("summary").value;

    if (!title || !discipline || !summary) {

        alert(translations[currentLang].alert_ai_fields);

        return;
    }

    const spinner = document.getElementById("ai-spinner");

    spinner.style.display = "inline-block";

    try {

        const response = await fetch(
            `${API_BASE_URL}/lesson-plans/ai-recommendations`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    title,
                    discipline,
                    summary
                })
            }
        );

        const result = await response.json();

        if (response.ok) {

            document.getElementById("contents").value =
                result.data.contents || "";

            document.getElementById("support_resources").value =
                result.data.support_resources || "";

            document.getElementById("tags").value =
                result.data.tags || "";

        } else {

            alert(
                `${translations[currentLang].alert_ai_error}${result.message}`
            );
        }

    } catch (error) {

        console.error("AI Error:", error);

        alert(translations[currentLang].alert_api_fail);

    } finally {

        spinner.style.display = "none";
    }
}

/* =========================================
   SAVE LESSON PLAN
========================================= */

async function saveLessonPlan(event) {

    event.preventDefault();

    const id = document.getElementById("plan-id").value;

    const payload = {
        title: document.getElementById("title").value,
        discipline: document.getElementById("discipline").value,
        objective: document.getElementById("objective").value,
        summary: document.getElementById("summary").value,
        planned_date: document.getElementById("planned_date").value,
        contents: document.getElementById("contents").value,
        support_resources: document.getElementById("support_resources").value,
        tags: document.getElementById("tags").value
    };

    const url = id
        ? `${API_BASE_URL}/lesson-plans/${id}`
        : `${API_BASE_URL}/lesson-plans`;

    const method = id
        ? "PUT"
        : "POST";

    try {

        const response = await fetch(url, {
            method,
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        if (response.ok) {

            alert(translations[currentLang].alert_save_success);

            document.getElementById("lesson-plan-form").reset();

            document.getElementById("plan-id").value = "";

            switchTab("list");

        } else {

            const result = await response.json();

            alert(JSON.stringify(result.errors || result.message));
        }

    } catch (error) {

        console.error("Save error:", error);
    }
}

/* =========================================
   EDIT PLAN
========================================= */

async function editPlan(id) {

    try {

        const response = await fetch(
            `${API_BASE_URL}/lesson-plans/${id}`
        );

        const plan = await response.json();

        document.getElementById("plan-id").value = plan.id;
        document.getElementById("title").value = plan.title;
        document.getElementById("discipline").value = plan.discipline;
        document.getElementById("objective").value = plan.objective;
        document.getElementById("summary").value = plan.summary;
        document.getElementById("planned_date").value = plan.planned_date;
        document.getElementById("contents").value = plan.contents || "";
        document.getElementById("support_resources").value =
            plan.support_resources || "";
        document.getElementById("tags").value = plan.tags || "";

        document.getElementById("form-title").innerText =
            translations[currentLang].form_title_edit;

        switchTab("form");

    } catch (error) {

        console.error("Edit error:", error);
    }
}

/* =========================================
   DELETE PLAN
========================================= */

async function deletePlan(id) {

    if (!confirm(translations[currentLang].alert_delete_confirm)) {
        return;
    }

    try {

        const response = await fetch(
            `${API_BASE_URL}/lesson-plans/${id}`,
            {
                method: "DELETE"
            }
        );

        if (response.ok) {

            alert(translations[currentLang].alert_delete_success);

            fetchLessonPlans();
        }

    } catch (error) {

        console.error("Delete error:", error);
    }
}

/* =========================================
   INITIALIZATION
========================================= */

document.addEventListener("DOMContentLoaded", () => {

    loadTheme();

    applyTranslations();

    fetchLessonPlans();

    const filterInput = document.getElementById("filter-value");

    let debounceTimer;

    filterInput.addEventListener("input", () => {

        clearTimeout(debounceTimer);

        debounceTimer = setTimeout(() => {

            fetchLessonPlans();

        }, 300);
    });
});