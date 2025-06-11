// Responsável por alternar o tema
const themeToggle = document.getElementById('theme-toggle');
const mobileThemeToggle = document.getElementById('mobile-theme-toggle');
const html = document.documentElement;

// Verifica a preferência de tema salva
const savedTheme = localStorage.getItem('theme') ||
                  (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');

// Aplica o tema salvo
if (savedTheme === 'dark') {
    html.classList.add('dark');
    document.querySelectorAll('.fa-moon').forEach(el => el.classList.add('hidden'));
    document.querySelectorAll('.fa-sun').forEach(el => el.classList.remove('hidden'));
}

// Função para alternar o tema
function toggleTheme() {
    const isDark = html.classList.toggle('dark');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
    document.querySelectorAll('.fa-moon').forEach(el => el.classList.toggle('hidden', isDark));
    document.querySelectorAll('.fa-sun').forEach(el => el.classList.toggle('hidden', !isDark));
}

// Event Listeners
if (themeToggle) themeToggle.addEventListener('click', toggleTheme);
if (mobileThemeToggle) mobileThemeToggle.addEventListener('click', toggleTheme);