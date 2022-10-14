export interface MainRouteType {
  title: string,
  children: Array<SubRouteType>,
}

export interface SubRouteType {
  title: string,
  route: string,
}
