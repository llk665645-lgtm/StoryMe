import { useQuery } from '@pinia/colada'
import { authApi } from '../api/auth'
import { useAuthStore } from '../stores/auth'

export function useCurrentUserQuery() {
    const auth = useAuthStore()

    return useQuery({
        key: ['user', auth.accessToken],
        query: () => authApi.getMe(auth.accessToken!),
        enabled: () => !!auth.accessToken,
    })
}
