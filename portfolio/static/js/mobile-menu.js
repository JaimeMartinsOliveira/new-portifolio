// Responsável pelo menu responsivo
const mobileMenuButton = document.getElementById('mobile-menu-button');
const mobileMenu = document.getElementById('mobile-menu');

// Alternar visibilidade do menu
if (mobileMenuButton) {
    mobileMenuButton.addEventListener('click', () => {
        if (mobileMenu) {
            mobileMenu.classList.toggle('hidden');
        }
    });
}