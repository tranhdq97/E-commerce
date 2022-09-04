export enum TokenEnum {
  access = "access",
  refresh = "refresh"
}

export enum TokenExpireEnum {
  access = 10,
  refresh = 100 * 24 * 60 * 60
}
