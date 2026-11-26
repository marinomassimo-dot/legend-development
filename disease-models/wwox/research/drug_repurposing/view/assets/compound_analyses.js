(() => {
  const section = document.getElementById("compound-analyses");
  if (!section) return;
  const input = section.querySelector("#ca-query");
  const groups = [...section.querySelectorAll(".ca-section")];
  const archive = section.querySelector(".ca-archive");
  const status = section.querySelector('[role="status"]');
  section.querySelector(".ca-search").hidden = false;
  input.addEventListener("input", () => {
    const query = input.value.trim().toLowerCase();
    let count = 0;
    for (const group of groups) {
      let matches = 0;
      for (const card of group.querySelectorAll(".ca-card")) {
        const label = card.querySelector("h4").textContent + " " + (card.querySelector(".ca-strand")?.textContent || "");
        card.hidden = !label.toLowerCase().includes(query);
        if (!card.hidden) matches++;
      }
      group.hidden = !matches;
      count += matches;
    }
    if (archive) archive.open = Boolean(query);
    status.textContent = query ? (count ? count + " matching compounds" : "No matching compounds") : "";
  });
  function revealCard() {
    const id = location.hash.slice(1);
    const target = id.startsWith("analysis-") && document.getElementById(id);
    if (target && archive?.contains(target)) archive.open = true;
  }
  window.addEventListener("hashchange", revealCard);
  revealCard();
})();
