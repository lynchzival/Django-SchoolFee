const tbody = $('#fee-table tbody');

function insert_fee(_this) {
    let desc = $(_this).parent().find('input[name="fee_desc"]').val();
    let amount = $(_this).parent().find('input[name="amount"]').val();
    let descs = tbody.find('td#desc').map(function() {
        return $(this).text().trim();
    }).get();

    if (desc === ""){
        alert("Please enter a description");
        return;
    }

    if (descs.includes(desc)) {
        alert("Duplicate fee description");
        return;
    }

    let elem = `
        <tr>
            <input type="hidden" name="fee_desc[]" value="${desc}">
            <input type="hidden" name="amount[]" value="${amount}">
            <td id="desc">
                <button type="button" class="d-none d-sm-inline-block btn btn-sm btn-danger mr-2"
                onclick="remove_fee($(this))">
                    <i class="fas fa-trash fa-sm text-white-50"></i>
                </button>
                ${desc}
            </td>
            <td id="amount">${amount}</td>
        </tr>
    `;
    tbody.append(elem);
    calculate_total();
}

function remove_fee(_this) {
    $(_this).parent().parent().remove();
    calculate_total();
    let desc = $(_this).parent().parent().find('td#desc').text().trim();
    let amount = $(_this).parent().parent().find('td#amount').text().trim();

    console.log(desc);

    $('#id_fee_desc').val(desc);
    $('#id_amount').val(amount);
}

function calculate_total() {
    let total = 0;
    tbody.find('tr').each(function() {
        total += parseFloat($(this).find('td#amount').text());
    });
    $('#id_total_amount').val(total);
    $('#fee-table tfoot tr td:nth-child(2)').text("$"+total);
}

function get_total_amount(url, cid){
    $.ajax({
        url: url,
        type: 'POST',
        data: {
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            'course_id': cid,
        }
    }).done(function(data) {
        $('#id_total_fee').val(data.data);
    }
    ).fail(function(data) {
        console.log(data);
    });
}

function get_outstanding_balance(url, eid){
    $.ajax({
        url: url,
        type: 'POST',
        data: {
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            'enroll_id': eid,
        }
    }).done(function(data) {
        $('#id_balance').val(data.data);
    }
    ).fail(function(data) {
        console.log(data);
    });
}

function printInvoice() {
    let divContents = document.getElementById("invoice").innerHTML;
    let a = window.open('', '', `height=${screen.availHeight}, width=${screen.availWidth}`);
    a.document.write(divContents);
    a.document.close();
    a.print();
}
