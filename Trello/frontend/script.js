async function createBoard() {
    const response = await fetch('/api/boards/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            title: 'New Board' // Можете добавить форму для запроса заголовка
        }),
    });

    if (response.ok) {
        const board = await response.json();
        alert(
Board created: ${board.title}
);
        // Здесь можно обновить список досок на странице
    } else {
        console.error('Error creating board:', response.statusText);
        alert(
Ошибка при создании доски: ${response.statusText}
);
    }
}