import { generalRequest } from '../../utilities';
import { url, port, entryPoint } from './server';

const URL = `http://${url}:${port}/${entryPoint}`;

const resolvers = {
	Query: {
		userByUsernameAndPassword: (_, { username, password }) =>
			generalRequest(`${URL}/${username}/${password}`, 'GET'),
	},
	Mutation: {
		createUser: (_, { user }) =>
			generalRequest(`${URL}/`, 'POST', user),
	}
};

export default resolvers;