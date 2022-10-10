import axios from "axios"
import type { File } from "@/interfaces/response/File"
import { FileManagementApiEnum } from "@/enum/api/FileManagement";
import { CommonApiEnum } from "@/enum/api/Common";


export default {
  namespaced: true,
  actions: {
    async getFile({}, fileId: string) {
      const resp: File = await axios.get(FileManagementApiEnum.detail.replace(CommonApiEnum.id, fileId));
      return resp.data.file
    }
  },
}
