import './App.css';
import { Navbar } from './components/Navbar';
import { Login } from './components/Login'
import { Progress } from './components/Progress';
import { LatestProb } from "./components/Latestprob";
import { Submission } from './components/Submission';
import { Tags } from './components/tags';

function App() {
  return (
    <div className="App">
        <Navbar />      
        {/* <Login /> */}
      <div className='Appbody'>
        <Progress />
        <LatestProb />
        <Submission />
        {/* <Tags /> */}
      </div>
    </div>
  );
}

export default App;
