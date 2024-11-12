$(document).ready(function() {
    // Установка CSRF-токена в заголовки AJAX
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/.test(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
            }
        }
    });

    // Функция для получения CSRF-токена из cookie
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Проверка, начинается ли cookie с имени
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Обработка добавления задачи
    $('#add-task-form').on('submit', function(e) {
        e.preventDefault();
        var form = $(this);

        $.ajax({
            type: form.attr('method'),
            url: form.attr('action'),
            data: form.serialize(),
            success: function(task) {
                var newTask = $('<li class="show" data-id="' + task.id + '">' + task.title +
                    ' <button class="btn btn-danger btn-sm float-right delete-btn"><i class="fas fa-trash"></i></button>' +
                    ' <button class="btn btn-primary btn-sm float-right mark-complete-btn"><i class="fas fa-check"></i></button>' +
                    '</li>');
                $('.task-list').append(newTask);
                newTask.addClass('show'); // Добавляем класс show для анимации
                form.trigger('reset'); // Сброс формы
            },
            error: function() {
                alert('Ошибка при добавлении задачи.');
            }
        });
    });

    // Обработка отметки задачи как завершенной
    $('.task-list').on('click', '.mark-complete-btn', function() {
        var taskLi = $(this).closest('li');
        var taskId = taskLi.data('id');

        $.ajax({
            url: '/toggle_task/' + taskId + '/',
            method: 'PUT',
            success: function() {
                taskLi.toggleClass('completed'); // Изменяем класс для визуального эффекта
            },
            error: function() {
                alert('Произошла ошибка при изменении задачи.');
            }
        });
    });

    // Обработка удаления задачи
    $('.task-list').on('click', '.delete-btn', function() {
        var taskLi = $(this).closest('li');
        var taskId = taskLi.data('id');

        deleteTask(taskId); // Вызов функции удаления с корректным taskId
    });

    function deleteTask(taskId) {
        if (confirm("Вы уверены, что хотите удалить эту задачу?")) {
            $.ajax({
                url: '/delete_task/' + taskId + '/', // URL должен быть правильным
                type: 'DELETE',
                success: function (response) {
                    // Успешное удаление - удаляем элемент из DOM
                    $('li[data-id="' + taskId + '"]').remove(); // Удаление задачи из списка
                },
                error: function (response) {
                    alert('Ошибка при удалении задачи.');
                }
            });
        }
    }
});