const analyzeBtn = document.getElementById("analyzeBtn");

analyzeBtn.addEventListener("click", async function () {

    const code = document.getElementById("codeInput").value;

    if (code.trim() === "") {
        alert("Please enter some code first.");
        return;
    }

    try {

        const response = await fetch("/analyze", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                code: code
            })
        });

        const tokens = await response.json();

        displayTokens(tokens);

    } catch (error) {

        console.error("Error:", error);

        alert("Something went wrong while analyzing the code.");
    }

});


function displayTokens(tokens) {

    const table = document.getElementById("tokenTable");
    const tokenCount = document.getElementById("tokenCount");

    table.innerHTML = "";

    tokens.forEach((token, index) => {

        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${index + 1}</td>
            <td>${token.lexeme}</td>
            <td>${token.token}</td>
            <td>${token.line}</td>
        `;

        table.appendChild(row);

    });

    tokenCount.textContent = `${tokens.length} Tokens`;
}