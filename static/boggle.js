let timerDisplay = document.querySelector("#timer-display");
let submitWordForm = document.querySelector("#submit_word_form");
let timeLeft = 60;

/**
 * ticks down the timer and removes the ability to guess afterwards
 * @param {} timeLeft 
 */
function updateTimer(timeLeft) {
    timerDisplay.innerText = `Time left: ${timeLeft}`
}

let timer = setInterval(function() {
    timeLeft -= 1;
    updateTimer(timeLeft);
    
    if (timeLeft === 0) {
        // no more guesses
        clearInterval(timer);
        submitWordForm.style.display = "none";
        alert("no more guesses");
    }
}, 1000);

/**
 * If the word is valid, then update the score
 * @param {} wordLength 
 */
async function getScore(wordLength) {
    // set score to a local variable here
    let amountToAdd = wordLength;
    const response = await axios.get("/get-score", {params: {addingAmount: amountToAdd}})
    let score = response.data.score;
    document.querySelector("#score").innerText = `Score: ${score}`
}

/**
 * get request to check if word is valid
 */
async function handleSubmitWord() {
    let submittedWord = document.querySelector("#submit_word_input");
    console.log(submittedWord.value);

    const response = await axios.get("/check-word", {params: {word: submittedWord.value}});
    alert(response.data.result);
    if (response.data.result === "ok") {
        getScore(submittedWord.value.length);
    }
}

/**
 * event listener for the submit button
 */
submitWordForm.addEventListener("submit", async function(event) {
    event.preventDefault();
    handleSubmitWord();
});