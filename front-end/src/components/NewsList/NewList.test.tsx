import { render, screen } from '@testing-library/react';
import NewsList from './NewsList';
import { NewsEntry } from '../../types/NewsEntry';
import '@testing-library/jest-dom';

const mockNews: NewsEntry[] = [
	{ number: 1, title: 'News 1', points: 100, commentsCount: 10 },
	{ number: 2, title: 'News 2', points: 200, commentsCount: 20 },
	{ number: 3, title: 'News 3', points: 300, commentsCount: 30 },
];

describe('NewsList Component', () => {
	beforeAll(() => {
		Object.defineProperty(window, 'matchMedia', {
			writable: true,
			value: jest.fn().mockImplementation(query => ({
				matches: false,
				media: query,
				onchange: null,
				addListener: jest.fn(),
				removeListener: jest.fn(),
				addEventListener: jest.fn(),
				removeEventListener: jest.fn(),
				dispatchEvent: jest.fn(),
			})),
		});
	});
	test('renders news list correctly', () => {
		render(<NewsList news={mockNews} />);
		mockNews.forEach((news) => {
			const row = screen.getByText(news.title).closest('tr');
			expect(row).toHaveTextContent(news.number.toString());
			expect(row).toHaveTextContent(`${news.points} points`);
			expect(row).toHaveTextContent(`${news.commentsCount} comments`);
		})
	});
});
