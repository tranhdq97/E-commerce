import axios from "axios";
import VueCookies from "vue-cookies";
import type { RegisterUser } from "@/interfaces/RegisterUser";
import type { AuthUser } from "@/interfaces/AuthUser";
import type { LoginPayload } from "@/interfaces/LoginPayload";
import type { Token } from "@/interfaces/response/Token";
import { TokenEnum, TokenExpireEnum } from "@/interfaces/enum/Token";
import { StaffApiEnum } from "@/interfaces/enum/api/Staff";

export interface AuthState {
  user: null | AuthUser
}

export default {
  namespaced: true,
  state: {
    user: null,
  } as AuthState,
  getters: {
    isAuthenticated: (state: AuthState) => !! state.user,
    stateUser: (state: AuthState) => state.user
  },
  actions: {
    async register({}, user: RegisterUser) {
      const resp = await axios.post(StaffApiEnum.staffCreate, user);
      return resp;
    },
    async login({}, payload: LoginPayload) {
      const resp: Token = await axios.post(StaffApiEnum.authToken, {
        email: payload.email,
        provider: 'staff',
        password: payload.password
      })
      VueCookies.set(TokenEnum.access, resp.data.access, TokenExpireEnum.access)
      VueCookies.set(TokenEnum.refresh, resp.data.refresh, TokenExpireEnum.refresh)
      return resp;
    },
    logout({}) {
      VueCookies.remove(TokenEnum.access)
      VueCookies.remove(TokenEnum.refresh)
    },
    async refreshToken({}) {
      const resp: Token = await axios.post(StaffApiEnum.authTokenRefresh, {
        refresh: VueCookies.get(TokenEnum.refresh)
      })
      VueCookies.set(TokenEnum.access, resp.data.access, TokenExpireEnum.access)
      VueCookies.set(TokenEnum.refresh, resp.data.refresh, TokenExpireEnum.refresh)
      return resp
    }
  }
}
