import { useEffect, useState } from 'react';
import { NewsEntry } from '../../types/NewsEntry';
import axios from 'axios';
import NewsList from '../../components/NewsList/NewsList';

import './Entries.css';
import { Skeleton } from 'antd';
import FilterSelector from '../../components/FilterSelector/FilterSelector';
import { FilterType } from '../../types/FilterType';

function Entries() {
	const [news, setNews] = useState<NewsEntry[] | undefined | null>(null);
	const [selectedFilter, setSelectedFilter] = useState<FilterType | undefined>(
		undefined,
	);

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

	const onFilterChange = (filter: FilterType | undefined) => {
		setSelectedFilter(filter);
		setNews(null);

		let apiRequestRoute = `/api/hacker-news-entries/`;

		if (filter) {
			apiRequestRoute += `?filter_request=${filter.toString()}`;
		}

		axios
			.get<NewsEntry[]>(apiRequestRoute)
			.then(response => {
				setNews(response.data);
			})
			.catch(() => {
				setNews(undefined);
			});
	};

	return (
		<div className='container'>
			<div className='filters'>
				<div>Filters:</div>
				<FilterSelector
					filter={selectedFilter}
					onFilterChange={onFilterChange}
				/>
			</div>
			<Skeleton loading={news === null} active>
				{(() => {
					if (news !== null) {
						return <NewsList news={news} />;
					}
				})()}
			</Skeleton>
		</div>
	);
}

export default Entries;
