<!doctype html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Hiren</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	{{ HTML::style('css/bootstrap.min.css') }}
</head>
<body>
	<nav class="navbar navbar-default " role="navigation">
		<div class="container-fluid">
			<div class="navbar-header">
				<a class="navbar-brand" href="#">Hiren URL Shortener</a>
			</div>
			<div class="pull-right navbar-text">Hi , {{ $username }}</div>
		</div>
	</nav>
	<div class="container">
		@yield('container')
	</div>
	{{ HTML::script('js/bootstrap.min.js') }}
</body>
</html>