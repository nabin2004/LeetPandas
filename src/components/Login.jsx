// Login.js

import React from 'react';

export const Login = () => {
  return (
    <div className="loginPanel">
        <p className='Logtext'>Enter your email</p>
      <input className='inputBox email' type="email" placeholder="email" />
        <p className='Logtext'>Enter your password</p>
      <input className='inputBox password' type='password' placeholder="password" />
      <div className='logb'>
        <button className='logButton'>Login</button>
        <button className='logButton'>SignUp</button>
      </div>

    </div>
  );
}
