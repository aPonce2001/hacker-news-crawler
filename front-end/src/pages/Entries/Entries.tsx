import { useEffect, useState } from 'react';
import { NewsEntry } from '../../types/NewsEntry';
import axios from 'axios';
import NewsList from '../../components/NewsList/NewsList';

import './Entries.css';
import { Skeleton } from 'antd';

function Entries() {
	const [news, setNews] = useState<NewsEntry[] | undefined | null>(null);

	useEffect(() => {
		axios
			.get<NewsEntry[]>('/api/hacker-news-entries')
			.then(response => {
				setNews(response.data);
			})
			.catch(() => {
				setNews(undefined);
			});
	}, []);

	return (
		<>
			<div className='entries'>
				<Skeleton loading={news === null} active>
					{(() => {
						if (news !== null) {
							return <NewsList news={news} />;
						}
					})()}
				</Skeleton>
			</div>
		</>
	);
}

export default Entries;
