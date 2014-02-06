<?php

class HomeController extends BaseController {

	/*
	|--------------------------------------------------------------------------
	| Default Home Controller
	|--------------------------------------------------------------------------
	|
	| You may wish to use controllers instead of, or in addition to, Closure
	| based routes. That's great! Here is an example controller method to
	| get you started. To route to this controller, just add the route:
	|
	|	Route::get('/', 'HomeController@showWelcome');
	|
	*/

	public function showWelcome()
	{
		return View::make('hello');
	}

	function get_unique_short_url(){
		//create gibrish string lol :D
		$shortened = base_convert(rand(10000,99999) , 10 , 36);

		//check if this random string already exists in database
		if(Url::where_shortened($shortened)->first()){
			get_unique_short_url();
		}
		return $shortened;
	}
    public function Hiren(){
    	$url = Input::get('URL') ;
    	//check if already exit in database
    	$record = Url::where_url($url)->first();
    	if($record){
    		return View::make('hiren.result')->with('shortened' , ($_SERVER['SERVER_NAME'] . '/' . $record->shortened ) );
    	}else{
      $row = Url::create(array(
    		'url' => $url,
    		'shortened' => get_unique_short_url()
    		)) ;
    }
    }

    public function result($shortened){
    	$row = Url::where_shortened($shortened)->first();
    	if(not_null($row)) return Redirect::to("/") ;
    	return Redirect::to($row->url);
    }
}