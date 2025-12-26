async function analyze() {
    const data = {
        action: Number(document.getElementById("action").value),
        comedy: Number(document.getElementById("comedy").value),
        drama: Number(document.getElementById("drama").value),
        scifi: Number(document.getElementById("scifi").value),
    };

    const response = await fetch("http://127.0.0.1:8000/recommend", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    const table = document.getElementById("resultTable");
    table.innerHTML = "";

    result.recommendations.forEach(item => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${item.title}</td>
            <td>${item.score}</td>
        `;
        table.appendChild(row);
    });

    document.getElementById("resultCard").classList.remove("hidden");
}
