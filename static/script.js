document.addEventListener('DOMContentLoaded', function () {
  loadTrees();

  const form = document.getElementById('treeForm');
  form.addEventListener('submit', function (e) {
    e.preventDefault();

    const tree = {
      name: document.getElementById('treeName').value,
      location: document.getElementById('location').value,
      date: document.getElementById('datePlanted').value,
      status: document.getElementById('status').value
    };

    fetch('/api/trees', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(tree)
    })
      .then(res => res.json())
      .then(() => {
        form.reset();
        loadTrees();
      });
  });
});

function loadTrees() {
  fetch('/api/trees')
    .then(res => res.json())
    .then(trees => {
      const list = document.getElementById('treeList');
      list.innerHTML = '';
      trees.forEach(tree => {
        const li = document.createElement('li');
        li.innerHTML = `
          <strong>${tree.name}</strong> - ${tree.location}<br>
          Date: ${tree.date}<br>
          Status: ${tree.status}<br>
          <button onclick="deleteTree(${tree.id})">❌ Delete</button>
          <br><br>
        `;
        list.appendChild(li);
      });
    });
}

function deleteTree(id) {
  fetch(`/api/trees/${id}`, {
    method: 'DELETE'
  })
    .then(res => res.json())
    .then(() => {
      loadTrees();
    });
}
