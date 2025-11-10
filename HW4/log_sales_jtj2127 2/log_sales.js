//Jordyn Jaffe jtj2127
let clients = [
    "Shake Shack",
    "Toast",
    "Computer Science Department",
    "Teacher's College",
    "Starbucks",
    "Subsconscious",
    "Flat Top",
    "Joe's Coffee",
    "Max Caffe",
    "Nussbaum & Wu",
    "Taco Bell"
];

let sales = [
    { "salesperson": "James D. Halpert", "client": "Shake Shack", "reams": 100 },
    { "salesperson": "Stanley Hudson", "client": "Toast", "reams": 400 },
    { "salesperson": "Michael G. Scott", "client": "Computer Science Department", "reams": 1000 }
];

// Hardcoded salesperson
const salesperson = "Jordyn Jaffe"; 

$(document).ready(function () {
    display_sales_list(sales);

    $("#trash").droppable({
        accept: ".draggable",
        classes: { "ui-droppable-hover": "ui-state-active" },
        drop: function (event, ui) {
            let id_dropped = $(ui.draggable[0]).data("id");
            delete_sale_by_index(parseInt(id_dropped));
        }
    });

    $("#submit_sale").click(submitSale);

    $("#enter_reams").keypress(function (e) {
        if (e.which == 13) {
            submitSale();
        }
    });

    $("#enter_client").autocomplete({
        source: clients
    });
});

function display_sales_list(sales) {
    $("#sales").empty();

    if (sales.length === 0) {
        $("#sales").append("<div class='row'><div class='col-md-4'>No Sales</div></div>");
        return;
    }

    $.each(sales, function (i, sale) {
        let row = $("<div class='row bottom_row_padding draggable' data-id='" + i + "'>");
        row.append("<div class='col-md-2'>" + sale.salesperson + "</div>");
        row.append("<div class='col-md-4'>" + sale.client + "</div>");
        row.append("<div class='col-md-2'>" + sale.reams + "</div>");

        let col_actions = $("<div class='col-md-3'>");
        let delete_button = $("<button class='btn btn-warning'>X</button>");

        // Set data-id for delete button
        delete_button.data("id", i).click(function () {
            let id = $(this).data("id");
            delete_sale_by_index(id);
        });

        col_actions.append(delete_button);
        row.append(col_actions);

        // Enable dragging
        row.draggable({
            revert: "invalid",
            cursor: "move"
        });

        // Ensure hover changes the cursor to move
        row.hover(
            function () { 
                $(this).css({ "background-color": "lightyellow", "cursor": "move" }); 
            }, 
            function () { 
                $(this).css({ "background-color": "", "cursor": "" }); 
            }
        );

        $("#sales").append(row);
    });
}


function submitSale() {
    $(".warning").remove();
    let client = $.trim($("#enter_client").val());
    let reams = $.trim($("#enter_reams").val());
    let no_error = true;
    let first_empty_field = null; // Track first empty field

    if (client === "") {
        $("#client_warning_div").append('<div class="warning">Client cannot be empty</div>');
        if (!first_empty_field) first_empty_field = "#enter_client"; // Set focus target
        no_error = false;
    }

    if (reams === "") {
        $("#reams_warning_div").append('<div class="warning">Reams cannot be empty</div>');
        if (!first_empty_field) first_empty_field = "#enter_reams"; // Set focus only if client isn't empty
        no_error = false;
    }

    if (reams !== "" && !$.isNumeric(reams)) {
        $("#reams_warning_div").append('<div class="warning">Reams must be a number</div>');
        if (!first_empty_field) first_empty_field = "#enter_reams"; // Set focus only if no earlier issue
        no_error = false;
    }

    if (!no_error) {
        $(first_empty_field).focus(); // Move cursor to the first empty field
        return;
    }

    // If no errors, proceed with adding the sale
    let new_sale = { salesperson, client, reams: parseInt(reams) };
    addSale(new_sale);
}


function addSale(new_sale) {
    sales.unshift(new_sale);
    display_sales_list(sales);
    if ($.inArray(new_sale.client, clients) < 0) clients.push(new_sale.client);
    $("#enter_client, #enter_reams").val("");
    $("#enter_client").focus();
}

function delete_sale_by_index(index) {
    sales.splice(index, 1);
    display_sales_list(sales);
}
