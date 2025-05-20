export default function menuHamburgue() {
    const hamburguer = document.querySelector(".hamburguer");
    const nav = document.querySelector(".nav");
    const links = document.querySelectorAll(".nav a");

    function toggleNav() {
        nav.classList.toggle("active");
    }

    function closeNav() {
        nav.classList.remove("active");
    }

    hamburguer.addEventListener("click", toggleNav);

    links.forEach(link => {
        link.addEventListener("click", closeNav);
    });
}