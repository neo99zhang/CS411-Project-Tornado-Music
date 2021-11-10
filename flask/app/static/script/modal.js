$(document).ready(function () {
    // example: https://getbootstrap.com/docs/4.2/components/modal/
    // show modal
    $('#task-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const taskID = button.data('source') // Extract info from data-* attributes
        const task = button.data('task') // Extract info from data-* attributes
        const tag = button.data('tag')

        const modal = $(this)
        if (taskID === 'New Task') {
            modal.find('.modal-title').text(taskID)
            $('#task-form-display').removeAttr('taskID')
        } else {
            modal.find('.modal-title').text('Edit Task ' + taskID)
            $('#task-form-display').attr('taskID', taskID)
        }

        if (task) {
            modal.find('.form-control1').val(task);
        } else {
           modal.find('.form-control1').val('');
        }
        if (tag) {
            modal.find('.form-control2').val(tag);
        } else {
           modal.find('.form-control2').val('');
        }
    })
    $('#task-modal1').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const taskID = button.data('source') // Extract info from data-* attributes
        const task = button.data('task') // Extract info from data-* attributes
        const tag1 = button.data('tag1')
        const tag2 = button.data('tag2')

        const modal = $(this)
        if (taskID === 'New Task') {
            modal.find('.modal-title').text(taskID)
            $('#task-form-display').removeAttr('taskID')
        } else {
            modal.find('.modal-title').text('Edit Task ' + taskID)
            $('#task-form-display').attr('taskID', taskID)
        }

        if (task) {
            modal.find('.form-control1').val(task);
        } else {
           modal.find('.form-control1').val('');
        }
        if (tag1) {
            modal.find('.form-control2').val(tag1);
        } else {
           modal.find('.form-control2').val('');
        }
        if (tag2) {
            modal.find('.form-control3').val(tag2);
        } else {
           modal.find('.form-control3').val('');
        }
    })

    $('#submit-task').click(function () {
        const tID = $('#task-form-display').attr('taskID');
        
        $.ajax({
            type: 'POST',
            url:  '/create',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'task': $('#task-modal').find('.form-control1').val(),
                'tag': $('#task-modal').find('.form-control2').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
        console.log(data);
    });
    $('#submit-task2').click(function () {
        const tID = $('#task-form-display').attr('taskID');
        
        $.ajax({
            type: 'POST',
            url:  '/update',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'task': $('#task-modal1').find('.form-control1').val(),
                'tag1': $('#task-modal1').find('.form-control2').val(),
                'tag2': $('#task-modal1').find('.form-control3').val()


            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
        console.log(data);
    });
    $('#submit-task3').click(function () {
        const tID = $('#task-form-display').attr('taskID');
        
        $.ajax({
            type: 'POST',
            url:  '/search',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'search': $('#task-modal2').find('.form-control1').val(),
                'plt': $('#task-modal2').find('.form-control2').val(),
            }),
            datatype: 'json',
            success: function (res) {
               
                alert("Sucess");
                window.location.href='/search'; // error，无法主动跳转
                // window.event.returnValue=false;
            },
            error: function () {
                console.log('Error');
            }
        });
       
    });

    $('.remove').click(function () {
        const remove = $(this)
        $.ajax({
            type: 'POST',
            url: '/delete/' + remove.data('source'),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.state').click(function () {
        const state = $(this)
        const tID = state.data('source')
        const new_state = "Todo"
        if (state.text() === "In Progress") {
            new_state = "Complete"
        } else if (state.text() === "Complete") {
            new_state = "Todo"
        } else if (state.text() === "Todo") {
            new_state = "In Progress"
        }

        $.ajax({
            type: 'POST',
            url: '/edit/' + tID,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'status': new_state
            }),
            success: function (res) {
                console.log(res)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

});