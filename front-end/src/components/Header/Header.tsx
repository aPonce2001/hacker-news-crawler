import './Header.css';

import logo from '/logo.svg'

function Header() {
	return (
		<header className='header'>
			<div className='logo'>
				<img height={32} src={logo} alt='Hacker News Crawler logo'></img>
				<span>Hacker News Crawler</span>
			</div>
		</header>
	);
}

export default Header;
