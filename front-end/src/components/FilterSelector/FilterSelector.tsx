import { Button } from 'antd';
import { FilterType } from '../../types/FilterType';

interface FilterSelectorProps {
	filter?: FilterType;
	onFilterChange: (filter: FilterType | undefined) => void;
}

function FilterSelector({ filter, onFilterChange }: FilterSelectorProps) {
	return (
		<>
			<Button
                id='title-words-greater-than-five-order-by-comments-desc-button'
				type={
					filter ===
					FilterType.TITLE_WORDS_GREATER_THAN_FIVE_ORDER_BY_COMMENTS_DESC
						? 'primary'
						: 'default'
				}
				onClick={() =>
					onFilterChange(
						filter ===
							FilterType.TITLE_WORDS_GREATER_THAN_FIVE_ORDER_BY_COMMENTS_DESC
							? undefined
							: FilterType.TITLE_WORDS_GREATER_THAN_FIVE_ORDER_BY_COMMENTS_DESC,
					)
				}
			>
				With more than 5 words in title ordered by number of comments
			</Button>
			<Button
                id='title-words-less-than-or-equals-to-five-order-by-points-desc-button'
				type={
					filter ===
					FilterType.TITLE_WORDS_LESS_THAN_OR_EQUALS_TO_FIVE_ORDER_BY_POINTS_DESC
						? 'primary'
						: 'default'
				}
				onClick={() =>
					onFilterChange(
						filter ===
							FilterType.TITLE_WORDS_LESS_THAN_OR_EQUALS_TO_FIVE_ORDER_BY_POINTS_DESC
							? undefined
							: FilterType.TITLE_WORDS_LESS_THAN_OR_EQUALS_TO_FIVE_ORDER_BY_POINTS_DESC,
					)
				}
			>
				With less than or equals to 5 words in title ordered by points
			</Button>
		</>
	);
}

export default FilterSelector;
