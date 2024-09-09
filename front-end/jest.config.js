const config = {
	verbose: true,
	passWithNoTests: true,
	preset: 'ts-jest',
	testEnvironment: 'jsdom',
    testMatch: ['**/?(*.)+(spec|test).[tj]s?(x)'],
};

export default config;
