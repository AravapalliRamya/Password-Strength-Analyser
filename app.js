function toggleTheme() {
    document.body.classList.toggle("dark");
    document.body.classList.toggle("light");
}

function analyzePassword() {
    const pwd = document.getElementById("password").value;

    if (pwd.length === 0) {
        document.getElementById("bar").style.width = "0%";
        document.getElementById("strength").innerText = "—";
        document.getElementById("entropy").innerText = "—";
        document.getElementById("time").innerText = "—";
        return;
    }

    fetch("/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ password: pwd })
    })
    .then(res => res.json())
    .then(data => {
        const bar = document.getElementById("bar");

        bar.style.width = data.percentage + "%";
        bar.style.background =
            data.percentage < 40 ? "#ef4444" :
            data.percentage < 70 ? "#f59e0b" :
            "#22c55e";

        document.getElementById("strength").innerText =
            data.strength + " (" + data.percentage + "%)";
        document.getElementById("entropy").innerText = data.entropy;
        document.getElementById("time").innerText = data.crack_time;
    });
}
