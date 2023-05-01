import { useEffect, useState } from 'react';
import axios from 'axios';

const useCollectData = (url) => {
    const [fetch, setFetching] = useState({ isFetching: false });
    //const [dataState, setDataState] = useState({ data: [] });
    const [dataState, setDataState] = useState(null);
    const [apiurl] = useState(url);

    useEffect(() => {
        fetch(apiurl)
          .then((res) => res.json())
          .then((data) => setDataState(data))
          .catch((error) => console.log(error));
      }, [apiurl, dataState]);

    return dataState;

};

export default useCollectData