<?php

require_once 'config.php';

if (!isset($_SESSION['user_id']) || $_SESSION['user_role'] !== 'admin') 
{
  	header('Location: logout.php');
  	exit();
}

if(isset($_GET['action'], $_GET['id']) && $_GET['action'] == 'delete')
{
	$stmt = $pdo->prepare("DELETE FROM allotments WHERE id = ?");
  	$stmt->execute([$_GET['id']]);
  	$_SESSION['success'] = 'Allotment Data has been removed';
  	header('location:allotments.php');
}

include('header.php');

?>

<div class="container-fluid px-4">
    <h1 class="mt-4">Allotments Management</h1>
    <ol class="breadcrumb mb-4">
    	<li class="breadcrumb-item"><a href="dashboard.php">Dashboard</a></li>
        <li class="breadcrumb-item active">Allotments Management</li>
    </ol>
    <?php

    if(isset($_SESSION['success']))
	{
		echo '<div class="alert alert-success">'.$_SESSION['success'].'</div>';

		unset($_SESSION['success']);
	}

    ?>
	<div class="card">
		<div class="card-header">
			<div class="row">
				<div class="col col-6">
					<h5 class="card-title">Allotments Management</h5>
				</div>
				<div class="col col-6">
					<div class="float-end"><a href="add_allotments.php" class="btn btn-success btn-sm">Add</a></div>
				</div>
			</div>
		</div>
		<div class="card-body">
			<div class="table-responsive">
				<table class="table table-bordered table-striped table-bordered" id="allotment-table">
					<thead>
						<tr>
							<td>ID</td>
							<th>Alloted to</th>
							<th>Flat Number</th>
							<th>Block Number</th>
							<th>Type</th>
							<th>Move in Date</th>
							<th>Move Out Date</th>
							<th>Created At</th>
							<th>Action</th>
						</tr>
					</thead>
					<tbody></tbody>
				</table>
			</div>
		</div>
	</div>
</div>

<script src="https://cdn.datatables.net/1.10.24/js/jquery.dataTables.min.js"></script>
<script src="https://cdn.datatables.net/1.13.2/js/dataTables.bootstrap5.min.js"></script>

<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.2/css/dataTables.bootstrap5.min.css">
<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.2.0/css/bootstrap.min.css">


<?php

include('footer.php');

?>

<script>

$(document).ready(function() {
    $('#allotment-table').DataTable({
        "processing": true,
        "serverSide": true,
        "ajax": {
        	url: 'action.php',
        	method:"POST",
        	data: {action : 'fetch_allotments'}
        },
        "columns": [
            { "data": "id" },
            { "data": "name" },
            { "data": "flat_number" },
            { "data": "block_number" },
            { "data": "flat_type" },
            { "data" : "move_in_date"},
            { "data" : "move_out_date"},
            { "data" : "created_at"},
            {
        		"data": null,
        		"render": function(data, type, row) {
          			return '<a href="edit_allotments.php?id='+row.id+'" class="btn btn-sm btn-primary">Edit</a>&nbsp;<button type="button" class="btn btn-sm btn-danger delete_btn" data-id="'+row.id+'">Delete</button>';
        		}
        	}
        ]
    });

    $(document).on('click', '.delete_btn', function(){
    	if(confirm("Are you sure you want to remove this flats data?"))
    	{
    		window.location.href = 'allotments.php?action=delete&id=' + $(this).data('id') + '';
    	}
    });
});

</script>