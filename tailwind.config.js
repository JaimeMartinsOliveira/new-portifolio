/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.{html,js}"],
  theme: {
    fontFamily: {
      'sans': ['Poppins', 'sans-serif']
    },
    extend: {
      height: {
        '90vh': '90vh',
      },
      keyframes: {
        seta: {
          '0%': { transform: 'translateY(0)' },
          '100%': { transform: 'translateY(10px)' },
        },
      },
      animation: {
        seta: 'seta 0.5s ease-in-out infinite alternate',
      },  
    },
  },
  plugins: [],
}

