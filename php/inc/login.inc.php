<?php 

echo '
<h2>Login</h2>

<form action="action_page.php" method="post">
  <div class="imgcontainer">
    <img src="../../pics/avatar-tux.svg" alt="Avatar" class="avatar">
  </div>

	<label for="uname">
		Username: 
	</label>
	<input type="text" placeholder="Nutzername eingeben" name="uname" required>

	<label for="upass">
		Password: 
	</label>
		<input type="password" placeholder="Password eingeben" name="upass" required>
	<button type="submit">Login</button>
	
	<label>
		<input type="checkbox" checked="checked" name="remember"> Remember me
 	</label>
  </div>

  <div class="container" style="background-color:#f1f1f1">
    <button type="button" class="cancelbtn">Cancel</button>
    <span class="psw">Forgot <a href="#">password?</a></span>
  </div>

</form>

';

?>
