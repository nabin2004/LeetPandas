

export function Navbar() {

  return (
  <div className='Navbar'>


<div className='Logo'>
  <h1 className="logo">LeetPandas</h1>
</div>

<div className='secondHeader'>
    <div className='listedNav'>
        <ul>
          <li>About</li>
          <li>Activity</li>
          <li>Problems</li>
          <li>Competitions</li>
          <li>Leaderboard</li>
        </ul>
      </div>

    <div className='search'>
      <input type='text' placeholder="Search"/>
      
    </div>
    </div>
  </div>
  )
}
