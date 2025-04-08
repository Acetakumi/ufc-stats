import './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState([]);
  const [index, setIndex] = useState(0);

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios.get('http://127.0.0.1:8080');
      setData(response.data);
    };
    fetchData();
  }, []);

  if (data.length === 0) {
    return <h1>Loading</h1>;
  }

  const Eventhandler = (event) => {
    setIndex(event.target.value);
  };


  return (
    <div className='background'>
      <select
        className="form-select  text-black d-block mx-auto"
        aria-label="Default select example"
        onChange={Eventhandler}
      >
        <option value="" disabled selected >Weight Class</option>
        <option value="0">{data[0].division}</option>
        <option value="1">{data[1].division}</option>
        <option value="2">{data[2].division}</option>
        <option value="3">{data[3].division}</option>
        <option value="4">{data[4].division}</option>
        <option value="5">{data[5].division}</option>
        <option value="6">{data[6].division}</option>
        <option value="7">{data[7].division}</option>
        <option value="8">{data[8].division}</option>
        <option value="9">{data[9].division}</option>
        <option value="10">{data[10].division}</option>
        <option value="11">{data[11].division}</option>
        <option value="12">{data[12].division}</option>
      </select>

      <div className="container text-center">
        {/* Champion card */}
        <div className="row mt-4">
          <div className="col-6 offset-3">
            <div className="card edit-card" style={{ width: '18rem', margin: '0 auto' }}>
              <img
                src={data[index].fighters[0].stats.imgUrl}
                className="card-img-top img-edit"
                alt={data[index].division + ' Champion'}
              />
              <div className="card-body">
              <p>
               <span className="champion-text"> 👑</span>
            </p>
            <p>{data[index].fighters[0].stats.category}</p>
            <p>{data[index].fighters[0].stats.name}</p>
            <p>{data[index].fighters[0].stats.nickname|| '—'}</p>
            <p>{`${data[index].fighters[0].stats.age} years old`}</p>
            <p>
              Record: {`${data[index].fighters[0].stats.wins}-${data[index].fighters[0].stats.losses}-${data[index].fighters[0].stats.draws}`}
            </p>
              </div>
            </div>
          </div>
        </div>

        {/* All other fighters */}
        <div className="row mt-5">
          {data[index].fighters.map((fighter, i) => {
            if (i === 0) return null; // Skip first fighter (champion)
            return (
              <div key={i} className="col-md-4 mb-4">
                <div className="card edit-card" style={{ width: '18rem', margin: '0 auto' }}>
                  <img
                    src={fighter.stats.imgUrl}
                    className="card-img-top img-edit"
                    alt={`${data[index].division} Fighter`}
                  />
                  <div className="card-body">
                  <p>Rank: {fighter.rank}</p>
                    <p>{fighter.stats.category}</p>
                    <p>{fighter.stats.name}</p>
                    <p>{fighter.stats.nickname || '—'}</p>
                    <p>{`${fighter.stats.age} years old`}</p>
                    <p>
                      Record: {`${fighter.stats.wins}-${fighter.stats.losses}-${fighter.stats.draws}`}
                    </p>

                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

export default App;
