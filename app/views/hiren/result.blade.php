@extends('hiren.master')
@section('container')
<div class="container">
	<div class="col-md-4 col-md-offset-3">
    {{ Form::open(array('url' => '/x' , 'role'=>'form' , 'class'=> "form-horizontal")) }}
    	<div class="form-group">
        {{ Form::label('url' , 'Your long URL ' ) }}
        </div>
        <div class="form-group">
        {{ Form::text('URL') }}
        </div>
        <div class="form-group">
        {{ Form::submit('Shorten' , array("class"=>"btn btn-default")) }}
        </div>
    </div>
    {{ Form::close() }}
    </div>
@endsection