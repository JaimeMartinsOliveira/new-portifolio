export default function buttonTop() {
    const scrollToButton = document.getElementById("scrollTopButton");
    const docElement = document.documentElement;

    function scrolltoTop() {
        docElement.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    }

    function handleScroll() {
        const scrollTotal = docElement.scrollHeight - docElement.clientHeight;
        const count = docElement.scrollTop / scrollTotal

        if (count > 0.1) {
            scrollToButton.classList.add("showBtn");
        } else {
            scrollToButton.classList.remove("showBtn");
        }
    }

    document.addEventListener("scroll", handleScroll)
    scrollToButton.addEventListener("click", scrolltoTop);

}