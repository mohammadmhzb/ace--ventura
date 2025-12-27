const sliders = ["action", "comedy", "drama", "scifi", "romance", "thriller", "fantasy", "mystery"];
const resultTable = document.getElementById("resultTable");
const resultCard = document.getElementById("resultCard");

// live update numbers
sliders.forEach(id => {
  const input = document.getElementById(id);
  const val = document.getElementById(id + "Val");
  input.oninput = () => val.textContent = input.value;
});

async function analyze() {
  const payload = {
  action: +action.value,
  comedy: +comedy.value,
  drama: +drama.value,
  scifi: +scifi.value,
  romance: +romance.value,
  thriller: +thriller.value,
  fantasy: +fantasy.value,
  mystery: +mystery.value
};

  const res = await fetch("http://127.0.0.1:8000/recommend", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });

  const data = await res.json();
  resultTable.innerHTML = "";

  data.recommendations.forEach(item => {
    resultTable.innerHTML += `
      <tr>
        <td>${item.title}</td>
        <td>${item.score.toFixed(3)}</td>
        <td>${item.angle}°</td>
      </tr>
    `;
  });

  resultCard.classList.remove("hidden");
}
