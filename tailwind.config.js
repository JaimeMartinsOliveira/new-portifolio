module.exports = {
  content: [
    './templates/**/*.html',
    './**/*.py'
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
const defaultTheme = require('tailwindcss/defaultTheme');

module.exports = {
  content: [
    './templates/**/*.html', // Certifique-se de que os templates estão incluídos!
    './**/*.py'
  ],
  theme: {
    extend: {
      typography: {
        DEFAULT: {
          css: {
            pre: {
              overflowX: 'auto', // Controla que os blocos de código rolam horizontalmente
              maxWidth: '100%', // Garante que o conteúdo respeite os limites do contêiner
            },
            blockquote: {
              borderLeftWidth: '0.25rem', // Estiliza blocos de citação
              paddingLeft: '1rem',
            },
          },
        },
      },
    },
  },
  plugins: [require('@tailwindcss/typography')],
};