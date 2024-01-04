import './progress.css'


export const Progress = () => {
  return (
    <div className="progressPanel">
        <h2>Progress</h2>
        <p>Success is not final, failure is not fatal: It is the courage to continue that counts</p>
        <div className='tillNow'>
            <p className='progText'>Solved</p><p className='progText'>Unsolved</p>
        </div>
    </div>
  );
}
