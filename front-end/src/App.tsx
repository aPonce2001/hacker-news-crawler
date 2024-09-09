import './App.css';
import Header from './components/Header/Header';
import Entries from './pages/Entries/Entries';

function App() {
	return (
		<>
			<Header />
			<main>
				<Entries />
			</main>
		</>
	);
}

export default App;
