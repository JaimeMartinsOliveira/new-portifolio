// Atualiza o contador de visitas local (para demonstração)
let localViewCount = parseInt(localStorage.getItem('portfolioLocalViewCount') || '0') + 1;
localStorage.setItem('portfolioLocalViewCount', localViewCount);
const viewCounter = document.getElementById('view-counter');
if (viewCounter) viewCounter.textContent = localViewCount;