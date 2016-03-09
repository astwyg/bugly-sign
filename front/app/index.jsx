import { Button, Input, Row } from 'react-bootstrap';
import React from 'react';
import ReactDOM from 'react-dom';


const ThisPage = React.createClass({
	getInitialState() {
    return {
      signBtnDisabled: true,
      showText : "请注意, 此项目是React和Flask结合的练习产品, 严禁用于非工作区域签到, 敬业光荣!",
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
  startSign (){
    this.setState({
      signBtnDisabled: true,
      showText: "正在签到, 请稍等..."
    });
    jQuery.ajax({
      url:"/api/sign",
      method:"POST",
      data: JSON.stringify({
        "iccid":this.refs.iccid.getValue(),
        "phone":this.refs.phone.getValue(),
        "password":this.refs.password.getValue()
      }),
      contentType:"application/json", 
      success: data => {
        this.setState({
          signBtnDisabled: false,
          showText: data
        });
      },
      error: (xml,e) => {
        this.setState({
          signBtnDisabled: false,
          showText: "发生如下错误: "+e
        });
      }
    })
  },
	render() {
		return(
			<div>
        <Row>
          <p className=" col-xs-12 col-md-6 col-md-offset-3 ">
            {this.state.showText}
          </p>
        </Row>
        <Row>
  				<form className="form-horizontal col-xs-12 col-md-6 col-md-offset-3	">
  					<Input type="text" label="iccid" labelClassName="col-xs-2" wrapperClassName="col-xs-10" onChange={this.handleInput} ref="iccid"/>
  					<Input type="text" label="手机号" labelClassName="col-xs-2" wrapperClassName="col-xs-10" onChange={this.handleInput} ref="phone" />
  					<Input type="password" label="密码" labelClassName="col-xs-2" wrapperClassName="col-xs-10" onChange={this.handleInput} ref="password" />
  					<Button bsStyle="primary" bsSize="lg" disabled={this.state.signBtnDisabled} className="col-xs-offset-4 col-xs-4" onClick={this.startSign}>Bugly签到</Button>
  				</form>
        </Row>
			</div>
		);
	}
});

ReactDOM.render(<ThisPage />, document.getElementById('page'));