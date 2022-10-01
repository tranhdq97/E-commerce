import axios from "axios";
import VueCookies from "vue-cookies";
import type { RegisterUser } from "@/interfaces/RegisterUser";
import type { AuthUser } from "@/interfaces/AuthUser";
import type { LoginPayload } from "@/interfaces/LoginPayload";
import type { Token } from "@/interfaces/response/Token";
import type { GetMe } from "@/interfaces/response/GetMe";
import { TokenEnum, TokenExpireEnum } from "@/interfaces/enum/Token";
import { CustomerApiEnum } from "@/interfaces/enum/api/Customer";
import { AuthApiEnum } from "@/interfaces/enum/api/Auth";
import { Provider } from "@/interfaces/enum/Provider";
import { AuthDispatchEnum, FileManagementDispatchEnum } from "@/interfaces/enum/Dispatch";
import { AuthMutationEnum } from "@/interfaces/enum/Mutation";

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
      const resp = await axios.post(CustomerApiEnum.create, user);
      return resp;
    },
    async login({ dispatch }, payload: LoginPayload) {
      const resp: Token = await axios.post(AuthApiEnum.authToken, {
        email: payload.email,
        provider: Provider.customer,
        password: payload.password
      })
      VueCookies.set(TokenEnum.access, resp.data.access, TokenExpireEnum.access)
      VueCookies.set(TokenEnum.refresh, resp.data.refresh, TokenExpireEnum.refresh)
      await dispatch(AuthDispatchEnum.getMe, null, {root: true})
      return resp;
    },
    logout({ commit }) {
      VueCookies.remove(TokenEnum.access)
      VueCookies.remove(TokenEnum.refresh)
      commit(AuthMutationEnum.setUser, user)
    },
    async refreshToken({}) {
      const resp: Token = await axios.post(AuthApiEnum.authTokenRefresh, {
        refresh: VueCookies.get(TokenEnum.refresh)
      })
      VueCookies.set(TokenEnum.access, resp.data.access, TokenExpireEnum.access)
      VueCookies.set(TokenEnum.refresh, resp.data.refresh, TokenExpireEnum.refresh)
      return resp
    },
    async getMe({ dispatch, commit }) {
      const resp: GetMe = await axios.get(
        AuthApiEnum.getMe,
        {
          headers: { Authorization: "Bearer " + VueCookies.get(TokenEnum.access) }
        }
      )
      const user: AuthUser = {
        email: resp.data.email,
        lastName: resp.data.info.last_name,
        photo: null,
      }
      if (resp.data.info.photo !== null) {
        const file: string = await dispatch(
          FileManagementDispatchEnum.getFile, resp.data.info.photo,
          { root: true }
        )
        user.photo = file
      }
      commit(AuthMutationEnum.setUser, user)
    },
  },
  mutations: {
    setUser(state, user: AuthUser) {
      state.user = user
    },
    removeUser(state) {
      state.user = null
    }
  }
}
