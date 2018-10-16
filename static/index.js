document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".slot-open").forEach(slot => {
    slot.addEventListener("click", (evt) => {
      if (!evt.target.classList.contains("slot-open"))
        return;
      document.querySelector("#form-datetime").value = evt.target.dataset.time;
      document.querySelector("#form-location").value = evt.target.dataset.location;
      document.querySelector("#form-datetime").dataset.id = evt.target.dataset.id;
      $("#signup").modal();
      $("#form-name").focus();
    });
  });

  document.querySelector("#submit-signup").onclick = () => {
    fetch("/signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        name: document.querySelector("#form-name").value,
        position: document.querySelector("#form-position").value,
        email: document.querySelector("#form-email").value,
        phone: document.querySelector("#form-phone").value,
        category: document.querySelector("#form-category-advising").checked ? "Advising" :
                (document.querySelector("#form-category-preschmooze").checked ? "Preschmooze" : "None Specified"),
        id: parseInt(document.querySelector("#form-datetime").dataset.id),
        time: document.querySelector("#form-datetime").value
      })
    })
    .then(res => {
      if (res.status != 200) {
        alert("There was an error. Please refresh and try again!");
        return;
      }
      document.querySelector("#appt-confirm-time").innerHTML = document.querySelector("#form-datetime").value;
      document.querySelector("#appt-confirm").style.display = "block";
      $(".slot[data-id=" + document.querySelector("#form-datetime").dataset.id + "]").removeClass("slot-open");
      $(".slot[data-id=" + document.querySelector("#form-datetime").dataset.id + "]").addClass("slot-filled");
      $("#signup").modal("hide");
    });
  };
});