@extends('hiren.master')
@section('container')
    <h1>Hello Hiren</h1>
    {{ Form::open(array('url' => '/x')) }}
        {{ Form::label('url' , 'Your long URL ') }}
        {{ Form::text('URL') }}
        {{ Form::submit('Shorten') }}
    {{ Form::close() }}
@endsection