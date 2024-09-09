import { Table } from 'antd';
import { NewsEntry } from '../../types/NewsEntry';
import { ColumnsType } from 'antd/es/table';

interface NewsListProps {
	news: NewsEntry[] | undefined;
}

function NewsList(newsProps: NewsListProps) {
	const columns: ColumnsType<NewsEntry> = [
		{
			title: '#',
			dataIndex: 'number',
			key: 'number',
		},
		{
			title: 'Title',
			dataIndex: 'title',
			key: 'title',
		},
		{
			title: 'Points',
			dataIndex: 'points',
			key: 'points',
			render: (points: number) => `${points} points`,
		},
		{
			title: 'Comments',
			dataIndex: 'commentsCount',
			key: 'commentsCount',
			render: (commentsCount: number) => `${commentsCount} comments`,
		},
	];

	return (
		<Table columns={columns} dataSource={newsProps.news} pagination={false} />
	);
}

export default NewsList;
