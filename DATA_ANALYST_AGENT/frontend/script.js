let uploadedFileName = "";

function uploadFile() {
  const file = document.getElementById("fileInput").files[0];
  const formData = new FormData();
  formData.append("file", file);

  fetch("http://localhost:8000/upload", {
    method: "POST",
    body: formData
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById("uploadStatus").innerText = data.message;
      uploadedFileName = data.filename;
    });
}

function askQuestion() {
  const question = document.getElementById("questionInput").value;
  const formData = new FormData();
  formData.append("question", question);
  formData.append("filename", uploadedFileName);

  fetch("http://localhost:8000/query", {
    method: "POST",
    body: formData
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById("answerOutput").innerText = data.answer;
    });
}
