import { render, screen, fireEvent } from '@testing-library/react';
import FilterSelector from './FilterSelector';
import { FilterType } from '../../types/FilterType';
import '@testing-library/jest-dom';

describe('FilterSelector', () => {
	const mockOnFilterChange = jest.fn();

	beforeEach(() => {
		mockOnFilterChange.mockClear();
	});

	test('renders the buttons with default styles when no filter is selected', () => {
		render(<FilterSelector onFilterChange={mockOnFilterChange} />);

		const firstButton = screen.getByText(
			'With more than 5 words in title ordered by number of comments',
		).closest('button');
		const secondButton = screen.getByText(
			'With less than or equals to 5 words in title ordered by points',
		).closest('button');

		// Check that both buttons are in the default style
		expect(firstButton).toHaveClass('ant-btn-default');
		expect(secondButton).toHaveClass('ant-btn-default');
	});

	test('renders the first button as primary when the first filter is selected', () => {
		render(
			<FilterSelector
				filter={FilterType.TITLE_WORDS_GREATER_THAN_FIVE_ORDER_BY_COMMENTS_DESC}
				onFilterChange={mockOnFilterChange}
			/>,
		);

		const firstButton = screen.getByText(
			'With more than 5 words in title ordered by number of comments',
		).closest('button');

		expect(firstButton).toHaveClass('ant-btn-primary');
	});

	test('calls onFilterChange with the correct filter when a button is clicked', () => {
		render(<FilterSelector onFilterChange={mockOnFilterChange} />);

		const firstButton = screen.getByText(
			'With more than 5 words in title ordered by number of comments',
		).closest('button');

		fireEvent.click(firstButton!);

		expect(mockOnFilterChange).toHaveBeenCalledWith(
			FilterType.TITLE_WORDS_GREATER_THAN_FIVE_ORDER_BY_COMMENTS_DESC,
		);
	});

	test('toggles filter off when the button is clicked again', () => {
		render(
			<FilterSelector
				filter={FilterType.TITLE_WORDS_GREATER_THAN_FIVE_ORDER_BY_COMMENTS_DESC}
				onFilterChange={mockOnFilterChange}
			/>,
		);

		const firstButton = screen.getByText(
			'With more than 5 words in title ordered by number of comments',
		).closest('button');

		fireEvent.click(firstButton!);

		expect(mockOnFilterChange).toHaveBeenCalledWith(undefined);
	});

	test('renders the second button as primary when the second filter is selected', () => {
		render(
			<FilterSelector
				filter={
					FilterType.TITLE_WORDS_LESS_THAN_OR_EQUALS_TO_FIVE_ORDER_BY_POINTS_DESC
				}
				onFilterChange={mockOnFilterChange}
			/>,
		);

		const secondButton = screen.getByText(
			'With less than or equals to 5 words in title ordered by points',
		).closest('button');

		expect(secondButton).toHaveClass('ant-btn-primary');
	});
});
