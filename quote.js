const quoteContent = document.getElementById("quote-content");

const quoteChoices = [
    "Where did Joe go after getting lost in a minefield? Everywhere.",
    "I have to use a stepladder because my real ladder left when I was 5.",
    "I made a website for orphans! It doesn't have a home page.",
    "I'm sorry and I apologize mean the same thing, except at a funeral.",
    "What's the hardest part of a vegetable to eat? The weelchair.",
    "Dating is like algebra. You look at your X and just wonder Y.",
    "What do you call an autistic kid with a gun? Special forces!",
];

var quoteChoice = Math.floor(Math.random() * quoteChoices.length);
quoteContent.textContent = quoteChoices[quoteChoice];