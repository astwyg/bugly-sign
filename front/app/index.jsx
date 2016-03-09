import { Button, Input } from 'react-bootstrap';
import React from 'react';
import ReactDOM from 'react-dom';


const ThisPage = React.createClass({
	getInitialState() {
    return {
      signBtnDisabled: true,
      form:{
      	iccid:"",
      	phone:"",
      	password:"",
      }
    };
  },
  handleInput(e){
  	if(this.refs.iccid.getValue().length>0 &&this.refs.phone.getValue().length>0 &&this.refs.password.getValue().length>0){
  		this.setState({signBtnDisabled: false});
  	}
  },
	render() {
		return(
			<div>
				<form className="form-horizontal col-xs-12 col-md-6 col-md-offset-3	">
					<Input type="text" label="iccid" labelClassName="col-xs-2" wrapperClassName="col-xs-10" onChange={this.handleInput} ref="iccid"/>
					<Input type="text" label="手机号" labelClassName="col-xs-2" wrapperClassName="col-xs-10" onChange={this.handleInput} ref="phone" />
					<Input type="password" label="密码" labelClassName="col-xs-2" wrapperClassName="col-xs-10" onChange={this.handleInput} ref="password" />
					<Button bsStyle="primary" bsSize="block" disabled={this.state.signBtnDisabled} className="col-xs-offset-4 col-xs-4">Bugly签到</Button>
				</form>
			</div>
		);
	}
});

ReactDOM.render(<ThisPage />, document.getElementById('page'));