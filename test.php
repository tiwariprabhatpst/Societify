<?php

require_once 'config.php';

if (!isset($_SESSION['user_id']) || $_SESSION['user_role'] !== 'admin') 
{
  	header('Location: logout.php');
  	exit();
}
include('header.php');

?>

<form method="post">
				  	<div class="mb-3">
					    <label for="flat_id">Flat Number</label>
					    <select id="flat_id" name="flat_id" class="form-control">
					    	<option value="">Select Flat</option>
						    <?php
						      	// Query to get flat numbers from flats table
								  $stmt = $pdo->prepare("SELECT * FROM flats ORDER BY id DESC");
								$stmt->execute();
								// Fetch the flat's details from the database
								$flats = $stmt->fetchAll(PDO::FETCH_ASSOC);
						      	 foreach($flats as $flat): ?>
      						<option value="<?php echo $flat['id']; ?>"><?php echo $flat['block_number'] . ' - ' . $flat['flat_number']; ?></option>
      						<?php endforeach; ?>
					    </select>
				  	</div>
                      </form>

                      <?php

include('footer.php');

?>